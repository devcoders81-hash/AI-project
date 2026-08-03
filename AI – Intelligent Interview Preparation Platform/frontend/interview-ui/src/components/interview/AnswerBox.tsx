interface Props {
  answer: string;
  setAnswer: (value: string) => void;
  onSubmit: () => void;
}

export default function AnswerBox({
  answer,
  setAnswer,
  onSubmit,
}: Props) {
  return (
    <div className="bg-white rounded-lg shadow p-6 mt-6">

      <textarea
        rows={8}
        className="w-full border rounded p-3"
        value={answer}
        onChange={(e) => setAnswer(e.target.value)}
        placeholder="Write your answer..."
      />

      <button
        className="mt-4 bg-blue-600 text-white px-6 py-2 rounded"
        onClick={onSubmit}
      >
        Submit Answer
      </button>

    </div>
  );
}