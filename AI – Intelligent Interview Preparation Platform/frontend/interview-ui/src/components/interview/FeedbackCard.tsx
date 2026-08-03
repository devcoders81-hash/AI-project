interface Props {
  feedback: string;
  score: number;
}

export default function FeedbackCard({
  feedback,
  score,
}: Props) {
  return (
    <div className="bg-green-50 border rounded-lg p-6 mt-6">

      <h2 className="text-xl font-bold">
        AI Feedback
      </h2>

      <p className="mt-3">
        {feedback}
      </p>

      <h3 className="mt-5 text-lg font-semibold">
        Score : {score}/10
      </h3>

    </div>
  );
}